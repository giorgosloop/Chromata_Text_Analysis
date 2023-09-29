from sentence_transformers import SentenceTransformer

class Sentiment_Analysis():

	def __init__(self, MODEL_ID, sentiments_list):
      
		####
		self.sents_el_en={"χαρά":"happiness", "λύπη":"sadness", "έκπληξη":"surprise", "φόβος":"fear", "θυμός":"anger", "απέχθεια":"disgust", "θετικό":"positive", "αρνητικό":"negative"}
		###

		self.MODEL_ID = MODEL_ID
		self.text = ""
		self.sentiments_list = sentiments_list
		self.sentiment_results = {}

		print('[INFO] Loading Sentiment-Analysis Model...')
		self.model = SentenceTransformer(self.MODEL_ID)	
	

	def run_sentiment_analysis(self, text):
	
		self.text = text
		
		text_list = [self.text for i in range(len(self.sentiments_list))]

		embeddings1 = self.model.encode(text_list, convert_to_tensor=True)
		embeddings2 = self.model.encode(self.sentiments_list, convert_to_tensor=True)

		#Compute cosine-similarities (clone repo for util functions)
		from sentence_transformers import util
		cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

		#Output the pairs with their score

		for i in range(len(text_list)):
		  self.sentiment_results[self.sents_el_en[self.sentiments_list[i]]] = cosine_scores[i][i].item()
		  #print("{} 		 {} 		 Score: {:.4f}".format(text_list[i], self.sentiments_list[i], cosine_scores[i][i]))
		  

		return self.sentiment_results

