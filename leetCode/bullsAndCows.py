class Solution(object):
    def getHint(self, secret, guess):

        secretHash = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
        guessHash = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

        for i in range(len(secret)):
            secretHash[secret[i]] += 1
            guessHash[guess[i]] += 1

        cows = 0
        for key in secretHash:
            if guessHash[key] > 0 and secretHash[key] > 0:
                cows += min(guessHash[key], secretHash[key])

        bulls = 0
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bulls += 1

        return str(bulls) + "A" + str(cows - bulls) + "B"

solution = Solution()
result = solution.getHint("1807", "7810")
print(result)
result = solution.getHint("1123", "0111")
print(result)
result = solution.getHint("1807", "7810")
print(result)
result = solution.getHint("1807", "7810")
print(result)
result = solution.getHint("1807", "7810")
print(result)
result = solution.getHint("1807", "7810")
print(result)
result = solution.getHint("1807", "7810")
print(result)
result = solution.getHint("1807", "7810")
print(result)