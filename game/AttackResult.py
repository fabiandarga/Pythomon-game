from game.objects.status import StatusChangeResult


class AttackResult:
    def __init__(self, attack_name: str, hp_lost: int, remaining_hp, status_changes: StatusChangeResult) -> None:
        self._attack_name = attack_name
        self._hp_lost = hp_lost
        self._remaining_hp = remaining_hp
        self._status_changes = status_changes

    @property
    def alive(self):
        return self._remaining_hp > 0

    @property
    def attack_name(self):
        return self._attack_name

    @property
    def hp_lost(self):
        return self._hp_lost

    @property
    def remaining_hp(self):
        return self._remaining_hp

    @property
    def status_changes(self):
        return self._status_changes
