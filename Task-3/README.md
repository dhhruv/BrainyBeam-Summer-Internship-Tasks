## Task-3

### Task-3(A)

**Aim:** Random module functions with explanation.
-   Random module:
    *   Random module in python is used to generate pseudo-random variables.
    *   It can generate random numbers as well as can select elements randomly from the list. 
    *   It can also shuffle elements of the specified list.
    *   Following is the example of random module functions and their usage are shown in [task3a.py]()

### Task–3(B)

**Aim:** Build a password generator program containing numbers, alphabets and characters.

### Task–3(C)

**Aim:** Write a note about NLP, NLU and NLG with example.


-   **NLP:**
    *   NLP stands for Natural Language Processing.
    *   NLP is a technique of machine learning which is used for making a computer understand, process and analyze as well as manipulate human language. It can also generate human language.
    *   NLP can be used in many real-life areas:
        1.  Auto – prediction: Google search predicts the results on the basis of NLP.
        2.  Sentiment Analysis: Obtaining the sentiment of user.
        3.  Machine Translation: To translate one language to another via a tool.
        4.  Speech Recognition: Google Vocalware or WebSpeech.
    *   NLP has two subsets:
        1.	NLU
        2.	NLG

-   **NLU:**
    *   NLU stands for Natural Language Understanding.
    *   NLU is a branch of NLP.
    *   It is mainly used to transform the natural human language to a machine-readable format.
    *   A computer with the capability of machine learning can operate NLU and analyze large datasets resulting into efficient analysis. 
    *   It mainly works on how a machine may analyze and understand an unstructured data.
    *   Example of NLU:
        1.  Question Answering 
        2.  Machine Translation
        3.  Data Capture

-   **NLG:**
    *   NLG stands for Natural Language Generation.
    *   NLG is a type of AI (Artificial Intelligence) which is used to generate natural language from a structured set of data.
    *   NLG is a subset of NLP and Machine learning, neural network as well as deep learning is used by NLG to generate natural language.
    *   Some of the applications of NLG are as follows:
        1.  Building Chatbots
        2.  Automated Lead Nurturing
        3.  Text Generation
        4.  Building Voice Assistants


-   NLU will initially try to understand the data based on:
    1.	Grammar
    2.	The context in which it was said
    3.	Decision on entities as well as intent.

-   NLP will convert the NLU generated text into structured data.
-   NLG will then generate text which is based on the NLP generated structured data.


 
-   **NLP Pipeline:**
1.	Text Information: Entering the sound converted to text or text.
2.	Segmentation and Tokenization: Segmentation of text into different components.
3.	Text Cleaning: Filtering garbage and discarding unnecessary components/elements.
4.	Vectorization and Feature Engineering: Transforming raw data into vector data.
5.	Text Lemmatization and Stemming: Removing last characters which are unwanted and applying lemma.
6.	Machine Learning Algorithms: To use ML Algorithms to train models.
7.	Interpretation of Result: Obtaining final result in structured form.

### Task-3(D)

**Aim:** Perform Text-To-Speech examples using gtts.


-   Regular Text-To-Speech:
```sh
from gtts import gTTS
greet=gTTS("Welcome to my world")
greet.save('voice.mp3')
```

-   Accent with Text-To-Speech (Example - 1):
```sh
from gtts import gTTS
tts_en = gTTS('hello', lang='en')
tts_fr = gTTS('bonjour', lang='fr') ## will follow the pronounciation of 'French'
with open('hello_bonjour.mp3', 'wb') as f:
    tts_en.write_to_fp(f)
    tts_fr.write_to_fp(f)
```

-   Accent with Text-To-Speech (Example - 2):
```sh
from gtts import gTTS
sen = gTTS('hello', lang='en')
sfr = gTTS('hola amigo, despasito', lang='es') ## will follow the pronounciation of 'Spanish'
with open('hola.mp3', 'wb') as f:
    sen.write_to_fp(f)
    sfr.write_to_fp(f)
```

-   Playing sound with the help of BytesIO:
```sh
from gtts import gTTS
from io import BytesIO
mp3_fp = BytesIO() ## will help playing the audio during execution
tts = gTTS('hello', lang='en')
tts.write_to_fp(mp3_fp)
```

-   Playing sound in slow motion:
```sh
from gtts import gTTS
sfr = gTTS('despasito, quiero respirar tu cuello, despasito, Deja que te diga cosas al oido Para que te acuerdes si no estas connmigo, despasito', lang='es', slow=False)
## will follow the pronounciation of 'Spanish' and in slow motion
with open('desp.mp3', 'wb') as f:
    sfr.write_to_fp(f)
``` 
