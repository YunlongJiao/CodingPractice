# NOTE
# Take absolute diff of hour and minute angles and subtract by 180 if larger than 180 degrees!


def clock_hands_angle(h, m):
    """
    Function to Calculate angle b/w hour hand and minute hand.

    """

    assert 0 <= h < 24
    assert 0 <= m < 60

    angle_hour = (h + m / 60) * 30
    angle_minute = m * 6

    angle = abs(angle_hour - angle_minute) % 180  # subtract by 180 in case of obtuse angles

    return angle


if __name__ == '__main__':
    h = 2
    m = 20
    print('Angle ', clock_hands_angle(h, m))