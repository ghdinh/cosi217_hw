import streamlit as st
from ner import SpacyDocument
import spacy
import pandas as pd
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

st.balloons()
st.title("NER using spacy")


def ner():
    # from new yorker article
    sent = "Long before the burglar Vjeran Tomic became the talk of Paris, he honed his skills in a graveyard. Père " \
           "Lachaise, the city’s largest cemetery, is a Gothic maze of tombstones, in the Twentieth Arrondissement, " \
           "that covers more than a hundred acres. Frédéric Chopin, Marcel Proust, and Oscar Wilde are among those " \
           "buried there. Tomic recalled that in the nineteen-eighties, when he was an adolescent, the cemetery " \
           "attracted hippie tourists, who flocked to the grave of Jim Morrison, and also drug dealers and gang " \
           "members. Tomic was drawn by the tombstones. In one of twenty letters, written in careful cursive French, " \
           "that he sent me during the past year and a half, he told me, “Observing them gave me the desire to touch " \
           "them—to climb up to their peaks.” Tomic and his friends turned the cemetery into a parkour playground, " \
           "leaping from the roof of one mausoleum to the next, daring one another to take ever-bolder risks. "
    doc = SpacyDocument(sent)
    entities = doc.get_entities()  # from entities method
    return sent, entities


def panda_dataframe(entities: list) -> pd.DataFrame:
    # entities = list of tuples with start_char, end_char, label_text
    return pd.DataFrame(data=entities, columns=['Start Char', 'End Char', 'Label', 'Text'])


if __name__ == "__main__":
    text, entities = ner()

    # display dataframe
    entities_dataframe = panda_dataframe(entities)
    st.dataframe(entities_dataframe)

    doc = nlp(text)
    st.header("Entity visualization")
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html, unsafe_allow_html=True)
