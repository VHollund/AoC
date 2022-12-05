def look_and_say(s, n):
  # Iterate n times
  for i in range(n):
    # Initialize the new sequence with the first digit of the old sequence
    new_seq = []
    # Keep track of the current digit and count
    curr_digit = s[0]
    curr_count = 1
    # Iterate over the rest of the old sequence
    for j in range(1, len(s)):
      # If the current digit is the same as the previous one, increment the count
      if s[j] == curr_digit:
        curr_count += 1
      # Otherwise, append the count and digit to the new sequence and reset the count
      else:
        new_seq.append(str(curr_count))
        new_seq.append(curr_digit)
        curr_digit = s[j]
        curr_count = 1
    # Append the count and digit of the last run to the new sequence
    new_seq.append(str(curr_count))
    new_seq.append(curr_digit)
    # Update the old sequence with the new one
    s = ''.join(new_seq)
  # Return the length of the final sequence
  return len(s)

# Test the function with the example input and 40 iterations
input = "1321131112"
iterations = 40
print(look_and_say(input, iterations))
iterations = 50
print(look_and_say(input, iterations))
