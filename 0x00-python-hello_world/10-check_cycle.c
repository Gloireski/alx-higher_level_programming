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
	if (list != NULL)
	{
		if (list->next != NULL)
			return (1);
		else
			return (0);
	}
	return (0);
}
