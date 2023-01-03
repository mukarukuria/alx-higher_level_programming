#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list checked if contains a cycle
 *
 * Return: 0 if no cycle, 1 if cycle exists
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *last = list;

	if (list == NULL)
		return (0);

	while (first->next != NULL && first->next->next != NULL)
	{
		first = first->next->next;
		last = last->next;
		if (first == last)
			return (1);
	}
	return (0);
}
