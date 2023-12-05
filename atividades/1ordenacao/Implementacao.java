public class Implementacao {

	public static void main(String[] args) {
		int []v = {7,4,15,14,2,16,9,8,13,11};
		InsertionSort(v)
	}

	//Força Bruta
	public static void InsertionSort(int []v) {
		int aux;
		int j;
		for(int i=1;i<v.length;i++) {
			aux=v[i];
			j=i;
			while(j>0 && v[j-1]<aux) {
				v[j]=v[j-1];
				j--;
			}
			v[j]=aux;
			imprime(v);
		}
	}

	//Divisão e Conquista
	public static void QuickSort(int[]v){
		QuickSort(v,0,v.length);
	}
	private static void QuickSort(int[]v,int p,int r) {
		if(p<r) {
			int q = Partition(v,p,r);
			QuickSort(v,p,q-1);
			QuickSort(v,q+1,r);
		}
	}
	private static int Partition(int[]v,int p,int r) {
		int x=v[r];
		int i=p-1;
		imprime(v);
		for(int j=p;j<r;j++) {
			if(v[j]>=x) {
				i++;
				int aux=v[i];
				v[i]=v[j];
				v[j]=aux;
				imprime(v);
			}
		}
		int aux=v[i+1];
		v[i+1]=v[r];
		v[r]=aux;
		imprime(v);
		return i+1;
	}

	//Força Bruta
	public static void BubbleSort(int []v) {
		imprime(v);
				for(int i=0;i<v.length-1;i++) {
					for(int j=0;j<v.length-1-i;j++) {
						if(v[j]<=v[j+1]) {
							int aux=v[j];
							v[j]=v[j+1];
							v[j+1]=aux;
							imprime(v);
						}
					}
				}
	}

	public static void imprime(int []v) {
		for(int i=0;i<v.length;i++) {
			System.out.print(v[i]+" ");
		}
		System.out.println();
	}
}