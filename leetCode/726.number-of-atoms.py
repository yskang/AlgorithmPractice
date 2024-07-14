#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#

from collections import defaultdict

# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        i = 0
        while i < len(formula):
            letter = formula[i]
            if letter == "(":
                stack.append(letter)
            elif letter == ")":
                f = []
                while stack[-1] != "(":
                    f.append(stack.pop())
                stack.pop()  # drop '(
                p_count = ''
                j = i+1
                while j < len(formula):
                    le = formula[j]
                    if le not in '0123456789':
                        break
                    p_count += le
                    j += 1
                i += len(p_count)
                p_count = int(p_count) if p_count else 1
                s = self.convert_2_atom(f, p_count)
                stack += s
            else:
                stack.append(letter)
            i += 1
        return self.convert_2_atom(list(reversed(stack)), 1)

    def convert_2_atom(self, formula: list, multi: int) -> str:
        atoms = defaultdict(lambda: 0)
        # formula.reverse()
        new_atom = ''
        count = ''
        while formula:
            letter = formula.pop()
            if letter.isupper():
                if new_atom != '':
                    atoms[new_atom] += (int(count) if count else 1) * multi
                new_atom = letter
                count = ''
            elif letter.islower():
                new_atom += letter
            elif letter.isdigit():
                count += letter
        if new_atom:
            atoms[new_atom] += (int(count) if count else 1) * multi
        atom_names = sorted(atoms.keys())
        result = ''
        for name in atom_names:
            result += f'{name}{atoms[name] if atoms[name] > 1 else ""}'
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.countOfAtoms("Mg(OH)2"))

        
# @lc code=end

# Atom starts Uppercase letter
# Atom is one uppercase letter followed by zero or more lowercase letters
# Number is 2 or more digits if atom is more than 1
# Number is 1 there will no digit


