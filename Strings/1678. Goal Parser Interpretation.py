# Example 1:

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# Example 2:

# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# Example 3:

# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"


class Solution:
    def interpret(self, command: str) -> str:
        if "()" in command:
            command = command.replace("()", "o")

        if "(al)" in command:
            command = command.replace("(al)", "al")

        return command


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
