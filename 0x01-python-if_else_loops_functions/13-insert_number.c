#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the said list
 * @number: number to be inserted to the list
 *
 * Return: address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current = *head;

	new->n = number;
	new->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	} else
	{
		while (current->next != NULL && current->next->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}

