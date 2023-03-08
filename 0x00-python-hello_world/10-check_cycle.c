#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list.
 * Return: 0 or 1.
 *
 */

int check_cycle(listint_t *list)
{
	int *node1, *node2;

	if (list == NULL)
		return (0);

	while (list != NULL)
	{
		node1 = (int *)&list;
		node2 = (int *)&list->next;
		if (list->next == NULL)
			return (0);

		if (*node1 - *node2 <= 0)
			return (1);

		list = list->next;
	}
	return (0);
}
