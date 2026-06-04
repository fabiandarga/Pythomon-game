from game.objects.Attack import Attack


class Scratch(Attack):
    _name = "Scratch"
    _damage = 10
    _cost = 0


SCRATCH = Scratch()