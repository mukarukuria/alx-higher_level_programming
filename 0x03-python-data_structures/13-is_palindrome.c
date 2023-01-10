#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 *
 * Return: 0 if not palindrome or 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *first = *head;
	listint_t *last = *head;
	listint_t *prev = NULL;
	listint_t *half = last->next;
	listint_t *first_half = *head;

	if (head == NULL || (*head)->next == NULL)
		return (1);
	while (first->next != NULL && first->next->next != NULL)
	{
		first = first->next->next;
		last = last->next;
	}


	last->next = NULL;
	listint_t *next;
	listint_t *current = half;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	half = prev;

	while (half != NULL)
	{
		if (first_half->n != half->n)
			return (0);

	first_half = first_half->next;
	half = half->next;
	}
	return (1);
}
