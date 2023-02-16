"""Defined a robot model """
from guilt_elimination_app.models import ranking
from guilt_elimination_app.views import console


DEFAULT_ROBOT_NAME = 'Donut Man'


class Robot(object):
    """Base model for Robot."""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='',
                 speak_color='cyan'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning."""
        while True:
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute({
                'robot_name': self.name}))

            if user_name:
                self.user_name = user_name.title()
                break


class GuiltEliminationRobot(Robot):
    """Handle data model on restaurant."""

    def __init__(self, name=DEFAULT_ROBOT_NAME):
        super().__init__(name=name)
        self.ranking_model = ranking.RankingModel()

    def _hello_decorator(func):
        """Decorator to say a greeting if you are not greeting the user."""
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper

    @_hello_decorator
    def did_you_eat_it(self):
        """Show restaurant recommended restaurant to the user."""
        new_did_you_eat_it = self.ranking_model.get_most_popular()
        if not new_did_you_eat_it:
            return None

        will_did_you_eat_it = [new_did_you_eat_it]
        while True:
            template = console.get_template('greeting.txt', self.speak_color)
            is_yes = input(template.substitute({
                'robot_name': self.name,
                'user_name': self.user_name,
                'restaurant': new_did_you_eat_it
            }))

            if is_yes.lower() == 'y' or is_yes.lower() == 'yes':
                break

            if is_yes.lower() == 'n' or is_yes.lower() == 'no':
                new_did_you_eat_it = self.ranking_model.get_most_popular(
                    not_list=will_did_you_eat_it)
                if not new_did_you_eat_it:
                    break
                will_did_you_eat_it.append(new_did_you_eat_it)

    @_hello_decorator
    def what_did_you_eat(self):
        """Collect favorite restaurant information from users."""
        while True:
            template = console.get_template(
                'question.txt', self.speak_color)
            food = input(template.substitute({
                'robot_name': self.name,
                'user_name': self.user_name,
            }))
            if food:
                self.ranking_model.increment(food)
                break

    @_hello_decorator
    def thank_you(self):
        """Show words of appreciation to users."""
        template = console.get_template('good_by.txt', self.speak_color)
        print(template.substitute({
            'robot_name': self.name,
            'user_name': self.user_name,
        }))

