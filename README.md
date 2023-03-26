# chatgpt on OpenIE

This repo evaluate chatgpt open information extraction performance using CaRB (a benchmark on OpenIE task).

## Poor result
chatgpt performs pretty poor on this task. It only achieve f1 of 0.248. On paperwithcode, the lowest score on this leaderboard is ~0.5 of f1 score. See more details [here](https://paperswithcode.com/sota/open-information-extraction-on-carb).

## Chatgpt settings
### api parameters
```text
model: gpt-3.5-turbo
messages.role: user
```
other settings are all the same as default settings.

### prompt
I input the following sentence to chatgpt on the brower, and choose one from its output.
```text
provide five concise prompts or templates that can make you deal with the open information extraction task and output the orig_sentence, head, relation, tail, output them in one line and use [TAB] to seperate them
```
So the input prompt to api is actually as follows, the input sentences is attach to it.
```text
"Prompt: Extract the relations between entities mentioned in the given sentence using open information extraction and output them in one line separated by tabs with head entity first. Output template: [ORIG_SENTENCE]\t[HEAD_ENTITY]\t[RELATION]\t[TAIL_ENTITY]\n"
```


## Post process
There are a lot of format problems in the raw output. So I do some post processing. The details are as follows.

- pick '\\t' as '\t'
- replace 'TAIL_ENTITY' by ''
- replace 'HEAD_ENTITY' by ''
- replace 'RELATION'/'Relation' by ''
- replace '|' by '\t'
- strip '(' and ')' for h,r,t
