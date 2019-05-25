# Bibliotecas para geração do Corpus
import nltk
# nltk.download() --> Utilizar este comando apenas 1x (Já foi utilizado)
from nltk.corpus import PlaintextCorpusReader

# Bibliotecas para geração da nuvem
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from nltk.corpus import stopwords
from wordcloud import WordCloud

# Bibliotecas para a Matriz de Termos Frequentes
import string

####################### CRIANDO A CORPUS #####################################

corpus = PlaintextCorpusReader('Arquivos', '.*')

#Para visualizar os arquivos pertencentes ao corpus:
arquivos = corpus.fileids()
arquivos[0]
arquivos[0:100]

for a in arquivos:
    print(a)

texto = corpus.raw('1.txt')

todo_texto = corpus.raw()
palavras = corpus.words() #Esta variável não aparece no variable explorer mas foi criada.
palavras[170]
len(palavras)


######################### GERANDO A NUVEM DE PALAVRAS #########################
stops = stopwords.words('english')
mapa_cores = ListedColormap(['orange', 'green', 'red', 'magenta'])
nuvem = WordCloud(background_color = 'white',
                  colormap = mapa_cores,
                  stopwords = stops,
                  max_words = 100)
nuvem.generate(todo_texto)

plt.imshow(nuvem)


##################### MATRIZ DE TERMOS MAIS FREQUENTES ########################

palavras_semstop = [p for p in palavras if p not in stops]
len(palavras_semstop)

palavras_sem_pontuacao = [p for p in palavras_semstop if p not in string.punctuation]
len(palavras_sem_pontuacao)

frequencia = nltk.FreqDist(palavras_sem_pontuacao)
mais_comuns = frequencia.most_common(100)

