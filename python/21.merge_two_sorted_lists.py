class Solution:
	def mergeTwoLists(self, l1, l2):
			it1, it2 = l1, l2
			dummy = ListNode(0)
			last = dummy

			while it1 and it2:
				if it1.val > it2.val:
					last.next = it2
					it2 = it2.next
				else:
					last.next = it1
					it1 = it1.next
				last = last.next

			last.next = it1 if it1 else it2

			return dummy.next