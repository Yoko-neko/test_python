"""Controller for speaking with robot"""
from guilt_elimination_app.models import robot


def talk_about_guilt_elimination():
    """Function to speak with robot"""
    guilt_elimination_robot = robot.GuiltEliminationRobot()
    guilt_elimination_robot.hello()
    guilt_elimination_robot.did_you_eat_it()
    guilt_elimination_robot.what_did_you_eat()
    guilt_elimination_robot.encourage_with_reason()
    guilt_elimination_robot.thank_you()