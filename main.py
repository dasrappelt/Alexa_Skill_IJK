Bio_Schneider = "Frau Professor Doktor Beate Schneider wurde 1947 in Fulda geboren und ist die ehemalige Direktorin des Instituts für Journalistik und Kommunikationsforschung der Hochschule für Musik, Theater und Medien Hannover."

Bio_Klimmt = "Herr Professor Doktor Christoph Klimmt wurde 1976 in Northeim geboren und war bis 2016 Direktor des Instituts für Journalistik und Kommunikationsforschung der Hochschule für Musik, Theater und Medien Hannover."

Bio_Scherer = "Herr Professor Doktor Helmut Scherer wurde 1955 in Zweibrücken geboren und ust seit 2016 Direktor des Instituts für Journalistik und Kommunikationsforschung der Hochschule für Musik, Theater und Medien Hannover."

Raum_127 = "Oh mann. Der Klassiker. Einfach die Stiegen rauf und dann rechts abbiegen. Schnurstracks geradeaus und ganz hinten links issa."

Info_Elevator = "Das wissen nur der Aufzug und Chuck Norris. Probieren geht hier wirklich über studieren."

Info_Theater = "Es wird dieses Jahr wieder eine AG geben. Aber Herr Reus macht es dieses Jahr wirklich zum letzten Mal."

Info_Wifi = "Dazu kann ich leider nichts sagen. Ein Teil dieser Antwort könnte die Studierenden verunsichern."

Info_Food = "Hm, auf jeden Fall gibt es heute Schnitzel."

Info_LSH = "Hm, die Arbeiten bei Frau Schneider meinst du? Wenn die Sonne im Westen aufgeht und im Osten versinkt, wenn die Meere austrocknen und die Berge wie Blätter im Wind verwehen."

Def_Medien = "Medien sind spezifische institutionalisierte Kommunikationskanäle. Nein. Warte. Medien sind komplexe Systeme mit gesellschaftlicher… Moment. Wie war das noch? Medien sind Leistungsvermögen mit Kanälen um Kommunikation von Relevanz in komplexen... error, error, error, Schalt mich aus, Schalt mich aus, Schnell. Bitte."

Lecture_PresseRundfunk = "Ich glaube, das war eine rhetorische Frage."

Hymne_IJK = "Wie macht das IJK? Das IJK macht so: Uh!"

Info_Home = "Kleiner Tipp: Nimm einfach am jährlich stattfindenden Running Dinner teil. mit ein wenig Glück kannst du es selbst herausfinden."

Info_FoodLater = "Sollte das 36 Grad Café schon geschlossen haben, könnte es problematisch werden. Hast du kein Proviant für lange Nächte voller Gruppenarbeit eingeplant, könnte die schlechte Laune während einer Gruppendiskussion unter Umständen auf den knurrenden Magen zurückzuführen sein. Fazit: Auf der Expo Plaza sollte man vorsorglich planen, denn Imbisse, Kioske oder Supermärkte sind weit und breit nicht in Sicht. Doch die Rettung im größten Notfall ist nahe: Der Süßigkeiten-Automat in der 1. Etage, der schon viele ausgehungerte Studenten und Studentinnen vor dem Durchdrehen bewahrte."

Info_Ort_Osterode = "Es stimmt alles. Und nun sprich es nie wieder an."

# ---------------------- Antwortaufbau ----------------------------------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }


# --------------- Funktionen zur Kontrolle des Skillverhaltens ------------------


def get_welcome_response():
    session_attributes = {}
    card_title = "Willkommen"
    speech_output = "Hallo, herzlich Willkommen am Institut für Journalistik und Kommunikationsforschung. Wie kann ich dir weiterhelfen?"
    reprompt_text = "Bitte stelle mir eine Frage."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_cancel_request():
    card_title = "Abbrechen"
    speech_output = "Ok, was willst du sonst?"
    should_end_session = False
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def handle_help_request():
    card_title = "Hilfe"
    speech_output = "Du brauchst wohl ein wenig Hilfe!"
    should_end_session = False
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def handle_session_end_request():
    card_title = "Session beenden"
    speech_output = "Okay, bis bald auf der Expo Plaza."
    should_end_session = True
    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


# ----------- Funktionen zur Beantwortung der definierten Fragen ---------

def get_bio_prof(intent):
    session_attributes = {}
    card_title = "BioProf"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "Name" in intent["slots"]:
        prof_name = intent['slots']['Name']['value']
        if prof_name.lower() == "schneider":
            speech_output = Bio_Schneider
        elif prof_name.lower() == "scherer":
            speech_output = Bio_Scherer
        elif prof_name.lower() == "klimmt":
            speech_output = Bio_Klimmt
        else:
            speech_output = "Was für eine Frage!"

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_raum_info(intent):
    session_attributes = {}
    card_title = "InfoRaum"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "Raum" in intent["slots"]:
        raum_name = intent['slots']['Raum']['value']
        if "27" in raum_name.lower():
            speech_output = Raum_127
        elif "121" in raum_name.lower():
            speech_output = 'Das weiß ich nicht.'
        else:
            speech_output = "Den Raum kenne selbst ich nicht."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_elevator_info(intent):
    session_attributes = {}
    card_title = "InfoElevator"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "Elevator" in intent["slots"]:
        elevator_name = intent['slots']['Elevator']['value']
        if elevator_name.lower() == "fahrstuhl":
            speech_output = Info_Elevator
        elif elevator_name.lower() == "aufzug":
            speech_output = Info_Elevator
        else:
            speech_output = "Das war jetzt ein wenig zu schnell. Bitte noch einmal."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_theater_info(intent):
    session_attributes = {}
    card_title = "InfoTheater"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "AG" in intent["slots"]:
        ag_name = intent['slots']['AG']['value']
        if ag_name.lower() == "theater":
            speech_output = Info_Theater
        elif ag_name.lower() == "ag":
            speech_output = Info_Theater
        else:
            speech_output = "Das habe ich nicht richtig kapiert."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_wifi_info(intent):
    session_attributes = {}
    card_title = "GetWifi"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "WIFI" in intent["slots"]:
        wifi_name = intent['slots']['WIFI']['value']
        if wifi_name.lower() == "wlan":
            speech_output = Info_Wifi
        elif wifi_name.lower() == "internet":
            speech_output = Info_Wifi
        elif wifi_name.lower() == "wifi":
            speech_output = Info_Wifi
        elif wifi_name.lower() == "internetz":
            speech_output = Info_Wifi
        else:
            speech_output = "Das kann und will ich nicht beantworten."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_food_info(intent):
    session_attributes = {}
    card_title = "GetFood"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "PlaceToEat" in intent["slots"]:
        food_name = intent['slots']['PlaceToEat']['value']
        if food_name.lower() == "mensa":
            speech_output = Info_Food
        elif food_name.lower() == "große pause":
            speech_output = Info_Food
        else:
            speech_output = "Piep, piep, wir haben uns alle lieb."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_lsh_info(intent):
    session_attributes = {}
    card_title = "InfoLSH"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "LSH" in intent["slots"]:
        lsh_name = intent['slots']['LSH']['value']
        if "lsh" in lsh_name.lower():
            speech_output = Info_LSH
        else:
            speech_output = "Ha ha ha ha ha ha."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_def(intent):
    session_attributes = {}
    card_title = "InfoDef"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "Begriff" in intent["slots"]:
        def_name = intent['slots']['Begriff']['value']
        if def_name.lower() == "medien":
            speech_output = Def_Medien
        else:
            speech_output = "Das kannst du mal schön selber durch definieren."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_lecture(intent):
    session_attributes = {}
    card_title = "InfoLecture"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "Vorlesung" in intent["slots"]:
        lecture_name = intent['slots']['Vorlesung']['value']
        if "presse" in lecture_name.lower() or "rundfunk" in lecture_name.lower():
            speech_output = Lecture_PresseRundfunk
        else:
            speech_output = "Frag mal Robyn."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_hymn(intent):
    session_attributes = {}
    card_title = "GetHymn"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "Hymn" in intent["slots"]:
        hymn_name = intent['slots']['Hymn']['value']
        if "ijk" in hymn_name.lower():
            speech_output = Hymne_IJK
        else:
            speech_output = "Hoch die Hände Wochenende oder was?"

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_home_info(intent):
    session_attributes = {}
    card_title = "InfoHome"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "Prof" in intent["slots"]:
        prof_name = intent['slots']['Prof']['value']
        if "schneider" in prof_name.lower():
            speech_output = Info_Home
        else:
            speech_output = Info_Home

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_food_later(intent):
    session_attributes = {}
    card_title = "GetFoodLater"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "PlaceToEatLater" in intent["slots"]:
        PlaceToEatLater_name = intent['slots']['PlaceToEatLater']['value']
        if "mensa" in PlaceToEatLater_name.lower() or "große pause" in PlaceToEatLater_name.lower():
            speech_output = Info_FoodLater
        else:
            speech_output = "Du bist verloren."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_ort_info(intent):
    session_attributes = {}
    card_title = "InfoOrt"
    reprompt_text = set_reprompt()
    should_end_session = False

    if "Ort" in intent["slots"]:
        Ort_name = intent['slots']['Ort']['value']
        if "osterode" in Ort_name.lower():
            speech_output = Info_Ort_Osterode
        else:
            speech_output = "Schwierige Frage."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------------------- Reprompt_Generierung -----------------------------

def set_reprompt():
    rueckgabe = "Wenn Du keine weiteren Fragen hast, beende bitte die Abfrage mit Stopp."
    return rueckgabe


# --------------------------------- Events -------------------------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Skill launch
    return get_welcome_response()


def on_intent(intent_request, session):

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Skill's intent handlers
    if intent_name == "BioProf":
        return get_bio_prof(intent)
    elif intent_name == "InfoRaum":
        return get_raum_info(intent)
    elif intent_name == "InfoElevator":
        return get_elevator_info(intent)
    elif intent_name == "InfoTheater":
        return get_theater_info(intent)
    elif intent_name == "GetWifi":
        return get_wifi_info(intent)
    elif intent_name == "GetFood":
        return get_food_info(intent)
    elif intent_name == "InfoLSH":
        return get_lsh_info(intent)
    elif intent_name == "InfoDef":
        return get_def(intent)
    elif intent_name == "InfoLecture":
        return get_lecture(intent)
    elif intent_name == "GetHymn":
        return get_hymn(intent)
    elif intent_name == "InfoHome":
        return get_home_info(intent)
    elif intent_name == "GetFoodLater":
        return get_food_later(intent)
    elif intent_name == "InfoOrt":
        return get_ort_info(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return handle_help_request()
    elif intent_name == "AMAZON.CancelIntent":
        return handle_session_cancel_request()
    elif intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return handle_session_end_request()


# ---------------------------- Main handler -----------------------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """

    # if (event['session']['application']['applicationId'] !=
    # al"applicationIdmissing"):
    # raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
