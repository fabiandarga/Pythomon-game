from game.objects.Attack import Attack


class Tackle(Attack):
    _name = "Tackle"
    _damage = 20
    _cost = 25


TACKLE = Tackle()