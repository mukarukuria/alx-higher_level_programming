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

	if (head == NULL || (*head)->next == NULL)
		return (1);
	while (first->next != NULL && first->next->next != NULL)
	{
		first = first->next->next;
		last = last->next;
	}
	listint_t *half = last->next;
	last->next = NULL;
	listint_t *current = half;
	listint_t *next;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	half = prev;
	listint_t *first_half = *head;
	while (half !=NULL)
	{
		if (first_half->n != half->n)
			return (0);

	first_half = first_half->next;
	half = half->next;
	}
	return (1);
}
	
