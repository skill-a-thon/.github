# -*- coding: utf-8 -*-

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from googletrans import Translator


LANGUAGE = "english"
SENTENCES_COUNT = 10


def summarize(text, line_count=10):
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    summarized = []

    for sentence in summarizer(parser.document, line_count):
        summarized += [str(sentence)]

    return '. '.join(summarized)




def translate(text, to_locale):

	translator = Translator(service_urls=['translate.googleapis.com'])
	translated = translator.translate(text, dest=to_locale)
	return translated.text




if __name__ == '__main__':
	text = """

World War I or the First World War, (28 July 1914 – 11 November 1918), often abbreviated as WWI, was one of the deadliest global conflicts in history. It was fought between two coalitions, the Allies (primarily France, the United Kingdom, Russia, Italy, Japan and the United States) and the Central Powers (led by Germany, Austria-Hungary, and the Ottoman Empire). Fighting occurred throughout Europe, the Middle East, Africa, the Pacific, and parts of Asia. An estimated 9 million soldiers were killed in combat, plus another 23 million wounded, while 5 million civilians died as a result of military action, hunger, and disease. Millions more died as a result of genocide, while the 1918 Spanish flu pandemic was exacerbated by the movement of combatants during the war.

The first decade of the 20th century saw increasing diplomatic tension between the European great powers. This reached breaking point on 28 June 1914, when a Bosnian Serb named Gavrilo Princip assassinated Archduke Franz Ferdinand, heir to the Austro-Hungarian throne. Austria-Hungary held Serbia responsible, and declared war on 28 July. Russia came to Serbia’s defence, and by 4 August, defensive alliances had drawn in Germany, France and Britain.

German strategy in 1914 was to first defeat France, then attack Russia. However, this failed, and by the end of 1914, the Western Front consisted of a continuous line of trenches stretching from the English Channel to Switzerland. The Eastern Front was more fluid, but neither side could gain a decisive advantage, despite a series of costly offensives. Attempts to bypass the stalemate caused fighting to expand into the Middle East, the Alps, the Balkans and overseas colonies, bringing Bulgaria, Romania, Greece and others into the war.

The United States entered the war on the side of the Allies in April 1917, while the Bolsheviks seized power in the Russian October Revolution, and made peace with the Central Powers in early 1918. Freed from the Eastern Front, Germany launched an offensive in the west on March 1918, hoping to achieve a decisive victory before American troops arrived in significant numbers. Failure left the German Imperial Army exhausted and demoralised, and when the Allies took the offensive in August 1918, they could not stop the advance.

Between 29 September and 3 November 1918, Bulgaria, the Ottoman Empire and Austria-Hungary agreed to armistices with the Allies, leaving Germany isolated. Facing revolution at home, and with his army on the verge of mutiny, Kaiser Wilhelm II abdicated on 9 November. The Armistice of 11 November 1918 brought the fighting to a close, while the Paris Peace Conference imposed various settlements on the defeated powers, the best-known being the Treaty of Versailles. The dissolution of the Russian, German, Austro-Hungarian and Ottoman Empires resulted in the creation of new independent states, among them Poland, Czechoslovakia, and Yugoslavia. Failure to manage the instability that resulted from this upheaval during the interwar period contributed to the outbreak of World War II in September 1939.

Names
The term world war was first coined in September 1914 by German biologist and philosopher Ernst Haeckel. He claimed that "there is no doubt that the course and character of the feared 'European War' ... will become the first world war in the full sense of the word,"[2] in The Indianapolis Star on 20 September 1914.

The term First World War (often abbreviated as WWI or WW1), had been used by Lt-Col. Charles à Court Repington, as a title for his memoirs (published in 1920); he had noted his discussion on the matter with a Major Johnstone of Harvard University in his diary entry of 10 September 1918.[3][4] Prior to World War II, the events of 1914–1918 were generally known as the Great War or simply the World War.[5][6] In August 1914, The Independent magazine wrote "This is the Great War. It names itself".[7] In October 1914, the Canadian magazine Maclean's similarly wrote, "Some wars name themselves. This is the Great War."[8] Contemporary Europeans also referred to it as "the war to end war" and it was also described as "the war to end all wars" due to their perception of its then-
	"""

	print(summarize(text, 1))