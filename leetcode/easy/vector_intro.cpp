#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;

int main()
{
    std::cout << "Test" << endl;

    /*
    int num;
    cin >> num;
    int arr[num];

    for (int i = 0; i < num; i++)
    {
        cin >> arr[i];
    }
    for (int i = num - 1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    } 
    */

   // /*
    std::size_t size{};
    std::cin >> size;
    std::vector<int> vect(size);

    std::cout << "Test2" << endl;

    for (std::size_t i{}; i < size; ++i)
        std::cin >> vect[i];


    // One of the many advantages to use C++ STL containers:
    // we can use reverse iterators
    for (auto rit = vect.rbegin(); rit != vect.rend(); ++rit)
        std::cout << *rit << ' ';
    std::cout << std::endl;
    // */

    return 0;
}