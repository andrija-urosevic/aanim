void selection_sort(int a[], const int n)
{
    for (int i = 0; i < n; i++) {
        int m = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[m]) {
                m = j;
            }
        }
        swap(a[i], a[m])
    }
}