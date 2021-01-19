# -*- coding:UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
from PIL import Image
import jieba

textfile =open("w.txt").read()
wordlist = jieba.cut(textfile,cut_all=True)
space_file = " ".join(wordlist)
background= np.array(Image.open("1.png"))
mywordcloud=WordCloud(background_color="white",
                mask=background,
                max_words=20,
                max_font_size=80,
                random_state=30,
                scale=1).generate(space_file)

image_color=ImageColorGenerator(background)
plt.imshow(mywordcloud)
plt.axis("off")
plt.show()
