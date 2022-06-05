
class TextEditor(object):

    def __init__(self):
        self.currentText = ""
        self.cursor = "|"
        self.position = 0
        
    def addText(self, text):
        newText = self.currentText[:self.position] + text + self.currentText[self.position:]
        self.cursor = newText[self.position]
        self.currentText = newText

    def deleteText(self, k):
        if self.position == 0:
            return 0
        k = min(k, self.position)
        newText = self.currentText[:self.position - k] + self.currentText[self.position:]
        self.cursor = newText[self.position - k]
        self.currentText = newText
        self.position -= k
        
        return k

    def cursorLeft(self, k):
        k = min(k, self.position)
        self.position -= k
        self.cursor = self.currentText[self.position]
        return self.currentText[self.position:self.position + k]

    def cursorRight(self, k):
        k = min(k, len(self.currentText) - self.position)
        self.position += k
        self.cursor = self.currentText[self.position]
        return self.currentText[self.position - k:self.position]
        


text = ["TextEditor","addText","deleteText","addText","cursorRight","cursorLeft","deleteText","cursorLeft","cursorRight"]
k = [[],["leetcode"],[4],["practice"],[3],[8],[10],[2],[6]]

obj = TextEditor()
obj.addText(text)
param_2 = obj.deleteText(k)
param_3 = obj.cursorLeft(k)
param_4 = obj.cursorRight(k)