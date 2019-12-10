import os, re

stories_files = None
for (dirname, dirs, files) in os.walk('./data/core'):
    stories_files = files

collections = set()
for s in stories_files:
    with open('./data/core/'+s) as story_raw:
        story = story_raw.read()
        intents = re.findall(r'\* .*', story)
        for intent in intents:
            intent_split = intent.split('OR')
            for i_split in intent_split:
                collections.add(i_split.replace('*', '').replace(' ', ''))

nlu_files = None

nlu_collections = set()
for n in os.listdir('./data/nlu'):
    with open('./data/nlu/'+n) as nlu_raw:
        nlu = nlu_raw.read()
        intents_nlu = re.findall(r'## intent:.*', nlu)
        for intent_nlu in intents_nlu:
            nlu_collections.add(intent_nlu.replace('## intent:', ''))

no_pair = set()
for c in collections:
    pair = False
    for n in nlu_collections:
        if c == n:
            pair = True
            break

    if not pair:
        no_pair.add(c)


with open('list_no_pair.txt', 'w') as w_f:
    w_f.write('\n'.join(no_pair))
