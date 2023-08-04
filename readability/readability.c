#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int ALPHABET[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
int count_letters(string text);
//int count_words(string text);
//int count_sentences(string text);

//int coleman_liau_formula(string letters,int words,int sentences);


int main(void)
{
    string text = get_string("Please enter your text: ");


    int letters = count_letters(text);
    //int words = count_words(text);
    //int sentences = count_sentences(text);

    printf("%s  %i\n", text, letters);
}


//counting letters, words, sentences

int count_letters(string text)
{
    int letter_count = 0;
    int len = strlen(text);

    for (int i = 0; i < len; i++)
    {
        if(isupper(text[i]))
        {
            letter_count += ALPHABET[text[i] - 'A'];
        }
    }
    return letter_count;

}



/*
int count_words(string text)
{

}



int count_sentences(string text)
{

}




int coleman_liau_formula(string letters,int words,int sentences);

{
    //max grade 16+ and min grade 1
}
*/

