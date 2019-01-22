from get_info import get_tournament_info


""" OLD MTT CLASS , rebuilding... """


class Mtt():
    print("DEBUG: MTT class initiated -- base class")

    def __init__(self, buyin, structure, starting_chips, initial_knockout, progressive_bounties):
        self.buyin = buyin
        self.structure = structure
        self.starting_chips = starting_chips
        self.initial_knockout = initial_knockout
        self.progressive_bounties = progressive_bounties
        # correct way to make info ? addon for child class?
        self.info = (f"${self.buyin} {self.structure} tournament with {self.starting_chips} starting chips.")  # ??

    def convert_bounty_to_chips(self):
        raise NotImplementedError("Subclass should complete conversions")


class StaticMtt(Mtt):
    """
    good approach? feels like this is using generic class mtt as a blueprint
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def convert_bounty_to_chips(self):
        print(f"{self.info}. Static knockouts. Each bounty is worth: ${self.initial_knockout}.")
        print(f"{self.initial_knockout/self.buyin:.0%}: value of each KO compared to buyin")
        self.true_bounty = self.initial_knockout / self.buyin * 2 * self.starting_chips
        print(f"{self.true_bounty} chips is the value of each knockout in this format.")

    def __str__(self):
        """ replace "self.info" with this ?? """
        return (f'{self.info} + ____ {self.true_bounty} chips per KO')


class ProgressiveKnockout(Mtt):
    """Since these tournaments require more conversions, assignments, use child classes."""

    # TODO: finish this

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        will require a 'while true' // break to keep prompting for displayed_bounty
        """
        self.displayed_bounty = my_tournament['progressive_bounties']['displayed_bounty']
        self.bounty_percent = my_tournament['progressive_bounties']['bounty_percent']
        print("DEBUG: PKO made")
        print("DEBUG: {}".format(self.info))  # should be default info for now
        #  These progressive tournaments require bounties that static bounties do not.
        # ie: bounty %, displayed_bounty, so add this to the 'template'

        self.info = self.info + (f"${self.displayed_bounty} bounty displayed. \
        {self.bounty_percent}%")

    def convert_bounty_to_chips(self):
        print(f"{self.info}. Static knockouts. Each bounty is worth: ${self.initial_knockout}.")
        print(f"{self.initial_knockout/self.buyin:.0%}: value of each KO compared to buyin")
        self.true_bounty = self.displayed_bounty / self.buyin / 2 * self.starting_chips
        print(f"{self.true_bounty} chips is the value of each knockout in this format.")

    def __str__(self):
        pass
        """ replace "self.info" with this ?? """

# def show_info(self):
#     self.info = (f"${self.buyin} {self.structure} tournament with {self.starting_chips} starting chips.")
#     if self.progressive_bounties['progressive_bounties']:  # if pko in dict is true
#         return self.info + (f" {self.progressive_bounties['bounty_percent']}% of each bounty cashed instantly\
#                         ${self.progressive_bounties['displayed_bounty']} bounty displayed. its effectively worth:\
#                         ${self.progressive_bounties['displayed_bounty'] * (self.progressive_bounties['bounty_percent'])/100}")
#
#     else:
#         return (self.info + " Static knockouts in this structure, no bounty increase.")
