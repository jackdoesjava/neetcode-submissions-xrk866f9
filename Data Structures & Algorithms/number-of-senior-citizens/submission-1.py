class Solution:
    def countSeniors(self, details: List[str]) -> int:
        oldies = 0
        for person in details:
            age = int(person[11:13]) # grab 11th and 12th index
            if age > 60:
                oldies += 1
        
        return oldies