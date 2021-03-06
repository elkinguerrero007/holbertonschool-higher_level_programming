#ifndef LISTS_H
#define LISTS_H

#define IS_PALINDROME 1
#define NOT_PALINDROME 0

#include <stdio.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *);
listint_t *add_nodeint_end(listint_t **, const int n);
void free_listint(listint_t *);
int is_palindrome(listint_t **);

#endif
