#include "lists.h"

/**
 * check_cycle - Check if a linked list has a cycle.
 *
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if a cycle is found, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
