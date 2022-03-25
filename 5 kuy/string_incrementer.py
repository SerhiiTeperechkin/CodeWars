def increment_string(strng):
    head = strng.rstrip('0123456789')
    foot = strng[len(head):]
    if foot == '': return strng + '1'
    return head + str(int(foot) + 1).zfill(len(foot))
