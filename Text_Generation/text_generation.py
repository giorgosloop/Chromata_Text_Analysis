import redis
import json
import time
import os

def text_generation(message):

    print(message)

    start_time = time.time()
    media_id = message["id"]
    path = os.getcwd() + "/Data/" + str(media_id) + "/"
    print('paaath:', path)
    os.makedirs(path, exist_ok=True)
    text_path = "/home/tpistola/Projects/Chromata/Services_v1/ASR2/Data/"+str(message['text_id'])+"/"+str(message['text_id'])+"_produced_text.txt"
    with open(text_path) as f:
        text = f.read()
    
    print('text:',text)
    #run text generation
    #...
    #...
    if text == 'gikna':
        text = """ Το είδος ειναι η Γικνα.  Το γένος του χορού είναι Ζωναράδικος. Η μορφή κινητικής ενότητας είναι Α+Α΄+Β, το σχήμα του
                 χορού είναι Ανοιχτός κύκλος με οδηγό και η κίνηση των χεριών είναι V+W. Χορεύεται στον Γάμο και το ένδυμα των χορευτών ειναι Γιορτινό."""

    elif text == 'mpaintouska':
        text = """
               Το είδος ειναι η Μπαϊντούσκα.  Το γένος του χορού είναι Μπαϊντούσκα. Η μορφή κινητικής ενότητας είναι Α+Β+Γ, το σχήμα του
                 χορού είναι Ανοιχτός κύκλος με οδηγό και η κίνηση των χεριών είναι V+W. 
                """
    elif text == 'karsilamas':
        text = """
              Το είδος ειναι ο Καρσιλαμάς.  Το γένος του χορού ειναι Καρσιλαμάς. Η μορφή κινητικής ενότητας είναι Α+Α, το σχήμα του χορού είναι ελεύθερο και η κίνηση των χεριών είναι ελύθερη. 
              Χορεύεται στον Γάμο και το ένδυμα των χορευτών ειναι Γιορτινό.
                """
    else:
        text = """Δεν υπάρχουν πληροφορίες για αυτόν τον χορό. Εσαγωγή ένός απο 'gikna', 'karsilamas', 'mpaintouska'. """
        #text = """
        #       H Γικνα ανηκει στο γενος των Ζωναραδικων. Η μορφη κινητικης ενοτητας ειναι Α+Α΄+Β, το σχημα του
        #         χορου ειναι Ανοιχτός κύκλος με οδηγό και η κινηση των χεριων V+W. Χορευεται στον Γαμο και το ενδυμα των χορευτων ειναι Γιορτινο
        #        """
    # --------------------------> Create output JSON with textgen information

    textgen_info = {}
    textgen_info["workspace"] = message["workspace"]
    textgen_info["id"] = message["id"]
    textgen_info["text_id"] = message["id"]
    textgen_info["project_id"] = message["project_id"]
    textgen_info["object_type"] = message["object_type"]
    textgen_info["text"] = text
    textgen_info["user_id"] = message["user_id"]
    textgen_info["sender"] = "text-generation"

    with open(path+'textgen_info_output.json', 'w', encoding='utf8') as outfile:
        json.dump(textgen_info, outfile, ensure_ascii=False)

    print("[INFO] Text-generation info output was saved in " + path + 'textgen_info_output.json')

    end_time = time.time()
    print("[INFO] Text-generation took {} seconds".format(end_time - start_time))

    # Send output json to 'completed-jobs' topic
    environment = 'completed-jobs'
    # action = outfile
    x = json.dumps(textgen_info)

    try:
        client = redis.Redis(host="", port=, password="")   # Need to add specific values here!
        client.publish(environment, x)
        print("[INFO] Text-generation result was successfully sent!")
    except Exception as e:
        print(f"ERROR:  {e}")

