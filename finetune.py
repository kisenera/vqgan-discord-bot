import gpt_2_simple as gpt2
from datetime import datetime
sess = gpt2.start_tf_sess()
gpt2.finetune(sess, '4chancut', steps=1000, model_name='345M')

#gpt2.finetune(sess,
 #             dataset="4chancut",
  #            model_name='345M',
   #           steps=8000,
    #          restore_from='fresh',
     #         run_name='4chan1',
      #        print_every=6,
       #       sample_every=100,
        #      save_every=250,
         #     only_train_transformer_layers = True,
          #    accumulate_gradients = 1,
           #   batch_size=1
            #  )