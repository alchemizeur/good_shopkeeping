def get_active_status(character):
    """Determine all active statuses of a character."""
    statuses = []

    if character.vitality <= character.max_vitality * 0.5:
        statuses.append("Injured")

    if character.equipped_slots.get("body") is None:
        statuses.append("Naked")

    return statuses