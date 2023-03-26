import tqdm
import pdb
import os
import openai

def ask_message(sent):
    prefix = "Prompt: Extract the relations between entities mentioned in the given sentence using open information extraction and output them in one line separated by tabs with head entity first. Output template: [ORIG_SENTENCE]\t[HEAD_ENTITY]\t[RELATION]\t[TAIL_ENTITY]\n"
    prompt = prefix+sent

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
    )

    with open('test_predict.tsv','a') as out_fp:
        out_fp.write(sent+'\n')
        out_fp.write(completion.choices[0].message['content']+'\n')
        out_fp.write('\n')




if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")

    with open('CaRB/data/test.txt') as fp:
        lines = fp.readlines()
        idx = 0
        for line in tqdm.tqdm(lines,desc='querying'):
            line = line.strip()
            ask_message(line)
            idx+=1