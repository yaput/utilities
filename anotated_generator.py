import pandas as pd
import re
import math

def find_start_end(entity, word, sentence, entity_values_text):
    """Use regex to find exact same word
    \nTODO: need to handle what if same entity value inside 1 sentence
    """
    res = []
    # Check if word not none
    if word is not None and entity is not None and entity_values_text is not None:
        # Split the words with ;, possible 1 sentence contain multiple entities with different value
        words = word.split(';')
        entity_values = entity_values_text.split(';')
        for i, w in enumerate(words):
            # Search the word in the sentence
            reg = re.search(w, sentence)
            # Get the start and end index for the word
            start, end = reg.span()
            # Append the object with entity format in RASA NLU format
            try:
                print(entity_values[i])
                entity_value_synonym = entity_values[i]
            except:
                entity_value_synonym = entity
            res.append({
                "value": entity_value_synonym,
                "start": start,
                "end": end,
                "entity": entity
            })

    return res

df = pd.read_csv('medcare-retrain.csv')

# Convert all panda dataframe to list
sentences = df['Sentence'].tolist()
intents = df['Intent'].tolist()
entities_values = df['Entity'].tolist()
entity_names = df['Entity Name'].tolist()
entity_real_value = df['Entity Real Value'].tolist()

# Final result of common example object in RASA NLU format
common_example = []

# Use enumerate list to get the index also
for index, sentence in enumerate(sentences):
    entity = entities_values[index]
    entity_name = entity_names[index]
    entity_value = entity_real_value[index]
    # Check if csv is empty or not, it will return `nan` if it's empty
    # If `nan` convert it to None, so it will meet find_start_end function parameter requirement
    try:
        if math.isnan(entity):
            entity = None
    except: 
        pass

    try:
        if math.isnan(entity_name):
            entity_name = None
    except:
        pass

    try:
        if math.isnan(entity_value):
            entity_value = None
    except:
        pass

    entity_info = find_start_end(entity_name, entity, sentence, entity_value)

    # User rasa json format for NLU training data
    ob = {
        "text": sentence,
        "intent": intents[index],
        "entities": entity_info
    }
    # append the object to list so we can save it
    common_example.append(ob)

import json
with open('new_training_data.json', 'w') as new_training_data:
    new_training_data.write(json.dumps(common_example, indent=3))