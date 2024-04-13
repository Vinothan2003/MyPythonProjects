class Text(str):  # Here extending the built-in data types, and not modifying them.
    def duplicate(self):
        return self + self


class TextList(list):
    def append(self, value):
        print("Append done...")
        super().append(value)

    def remove(self, __value):
        print("Remove done..")
        super().remove(__value)

    def len(self):
        print(super().__len__())
        print(len(self))


text = Text("Vinothan")
print(text.duplicate())

print(Text.duplicate(text))  # another way of sending the instance to class

text_list = TextList()
TextList.append(text_list, "Vinothan")
text_list.append('NC')
# text_list.remove("NC")
text_list.len()

print(text_list)
