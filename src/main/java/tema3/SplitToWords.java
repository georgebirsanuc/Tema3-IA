package tema3;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.Charset;
import java.util.Arrays;
import java.util.List;
import java.util.Properties;

import com.google.common.io.Files;

import edu.stanford.nlp.ling.CoreAnnotations.SentencesAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TextAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TokensAnnotation;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.util.CoreMap;

/**
 * A simple corenlp example ripped directly from the Stanford CoreNLP website
 * using text from wikinews.
 */
public class SplitToWords {

	public static void main(String[] args) throws IOException {
		String xml = "<words>\n";
//		String[] punctuation = { ".", ",", "!", "?", ":", ";", "\\", "/", "\"", "(", ")", "[", "]", "{", "}", "-", "+",
//				"=", "_", "#", "$", "%", "^", "&", "*", "~" };

		// creates a StanfordCoreNLP object, with POS tagging, lemmatization,
		// NER, parsing, and coreference resolution
		Properties props = new Properties();
		props.put("annotators", "tokenize, ssplit, pos, lemma, ner, parse, dcoref");
		StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

		// read some text from the file..
		File inputFile = new File("src/main/resources/sample-content.txt");
		String text = Files.toString(inputFile, Charset.forName("UTF-8"));

		System.out.println("NO PUNCT.: " + text);
		// create an empty Annotation just with the given text
		Annotation document = new Annotation(text);

		// run all Annotators on this text
		pipeline.annotate(document);

		// these are all the sentences in this document
		// a CoreMap is essentially a Map that uses class objects as keys and
		// has values with custom types
		List<CoreMap> sentences = document.get(SentencesAnnotation.class);

		for (CoreMap sentence : sentences) {
			// traversing the words in the current sentence
			// a CoreLabel is a CoreMap with additional token-specific methods
			for (CoreLabel token : sentence.get(TokensAnnotation.class)) {
				// this is the text of the token
				String word = token.get(TextAnnotation.class);
				// this is the POS tag of the token
				// String pos = token.get(PartOfSpeechAnnotation.class);
				// this is the NER label of the token
				// String ne = token.gets(NamedEntityTagAnnotation.class);

				xml += "\t<word> " + word + " </word>\n";
				// System.out.println("word: " + word + " pos: " + pos + " ne:"
				// + ne);
			}

			// this is the parse tree of the current sentence
			// Tree tree = sentence.get(TreeAnnotation.class);
			// System.out.println("parse tree:\n" + tree);

			// this is the Stanford dependency graph of the current sentence
			// SemanticGraph dependencies =
			// sentence.get(CollapsedCCProcessedDependenciesAnnotation.class);
			// System.out.println("dependency graph:\n" + dependencies);
		}
		
		xml += "</words>\n";
		System.out.println(xml);
		PrintWriter writer = new PrintWriter("src/main/resources/nlp.xml", "UTF-8");
		writer.print(xml);
		writer.close();

	}

}
