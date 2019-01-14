###
# peaks_and_valleys.py
# In class solution to lab 18: peaks and valleys
# Takes in as input a list of heights
# Returns the indices of peaks and valleys
###

def peaks(heights):
    """
    returns the indices of peaks
    """
    peaks = []
    # because we are comparing three items at once, 
    # we don't include the first and last indices
    for i in range(1,len(heights)-1):
        left = heights[i-1]
        middle = heights[i]
        right = heights[i+1]
        if left < middle > right:
            peaks.append(i)
    return peaks


def valleys(heights):
    """
    returns the indices of valleys
    """
    valleys = []
    for i in range(1,len(heights)-1):
        left = heights[i-1]
        middle = heights[i]
        right = heights[i+1]
        if left > middle < right:
            valleys.append(i)
    return valleys


def peaks_and_valleys(heights):
    """
    returns the indices of peaks and valleys in order appearance in the original data
    """
    p = peaks(heights)
    v = valleys(heights)
    return sorted(p + v)


def draw(heights):
    """
    returns string representation of mountain
    """
    mountain = []
    peak = max(heights)
    while peak > 0:
        row = ['X' if height >= peak else ' ' for height in heights]
        mountain.append(''.join(row))
        peak -= 1
    return '\n'.join(mountain)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(data)
    print(draw(data))
    print('peaks', peaks(data))              # → [6, 14]
    print('valleys', valleys(data))            # → [9, 17]
    print('peaks_and_valleys', peaks_and_valleys(data))  # → [6, 9, 14, 17]
    print()

    data = [1, 1, 1, 1, 1]
    print(data)
    print(draw(data))
    print('peaks', peaks(data))              # → [] empty list
    print('valleys', valleys(data))            # → []
    print('peaks_and_valleys', peaks_and_valleys(data))  # → []
    print()

    data = [3, 2, 1, 2, 3]
    print(data)
    print(draw(data))
    print('peaks', peaks(data))              # → [] empty list
    print('valleys', valleys(data))            # → [2]
    print('peaks_and_valleys', peaks_and_valleys(data))  # → [2] 
    print()

    data = [1, 2, 3, 2, 1]
    print(data)
    print(draw(data))
    print('peaks', peaks(data))              # → [2] 
    print('valleys', valleys(data))            # → []
    print('peaks_and_valleys', peaks_and_valleys(data))  # → [2] 