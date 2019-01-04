# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import speedtest

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

class SpeedTestSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(SpeedTestSkill, self).__init__(name="SpeedTestSkill")
        
        # Initialize working variables used within the skill.
        self.s = speedtest.Speedtest()

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'

    @intent_handler(IntentBuilder("").require("Speed"))
    def handle_count_intent(self, message):
        print(message)
        servers = []
        self.s.get_servers(servers)
        self.s.get_best_server()
        self.s.download()
        self.s.upload()
        self.s.results.share()

        results_dict = self.s.results.dict()
        print(results_dict)
        # if message.data["Dir"] == "up":
        #     self.count += 1
        # else:  # assume "down"
        #     self.count -= 1
        self.speak_dialog("test.results.are", data={"count": results_dict})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return SpeedTestSkill()
