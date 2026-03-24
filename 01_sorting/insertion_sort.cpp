void insertion_sort(int a[], const int n)
{
    for (int i = 1; i < n; i++) {
        int j = i;
        while (j > 0 && a[j] < a[j - 1]) {
            swap(a[j], a[j - 1])
            j--;
        }
    }
}