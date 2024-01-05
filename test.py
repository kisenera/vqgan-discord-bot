import gpt_2_simple as gpt2
import asyncio, random, string
import requests
import os

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='345M') # The name of your checkpoint

gentext = (gpt2.generate(sess, run_name="345M", temperature=0.9, nsamples=1, batch_size=1, prefix="", length=132, include_prefix=False, return_as_list=True))
gentexted = ' '.join(gentext)
print(gentexted)