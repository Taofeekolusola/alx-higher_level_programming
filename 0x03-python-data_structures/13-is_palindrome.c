#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = n;
	new_node->next = *head;
	*head = new_node;
	return (new_node);
}
/**
*is_palindrome - identify if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	listint_t *a = NULL, *a2 = NULL;

	if (*head == NULL || head2->next == NULL)
		return (1);
	while (head2 != NULL)
	{
		add_nodeint(&a, head2->n);
		head2 = head2->next;
	}
	a2 = a;
	while (*head != NULL)
	{
		if ((*head)->n != a2->n)
		{
			free_listint(a);
			return (0);
		}
		*head = (*head)->next;
		a2 = a2->next;
	}
	free_listint(a);
	return (1);
}
