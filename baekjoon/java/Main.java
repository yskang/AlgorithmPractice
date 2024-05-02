import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuffer ret = new StringBuffer();
	private static StringTokenizer st;
	private static int T = 1, C, N, P;
	private static long a[], t[], wv[][], max;

	public static void main(String[] args) throws IOException {
//		T = Integer.parseInt(br.readLine());
		while (T-- > 0) {
			set_input();
			solve();
		}

		System.out.println(ret);
	}

	private static void set_input() throws IOException {
		C = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		P = Integer.parseInt(st.nextToken());
		a = new long[N + 1];
		t = new long[N + 1];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			a[i] = Integer.parseInt(st.nextToken());
			t[i] = Integer.parseInt(st.nextToken());
		}
		wv = new long[P + 1][2];
		int r, p1;
		long _w, _v, p2;
		for (int i = 1; i <= P; i++) {
			_w = _v = 0;
			st = new StringTokenizer(br.readLine());
			r = Integer.parseInt(st.nextToken());
			for (int j = 0; j < r; j++) {
				p1 = Integer.parseInt(st.nextToken());
				p2 = Long.parseLong(st.nextToken());
				_w += a[p1] * p2;
				_v += (t[p1] - a[p1]) * p2;
			}
			wv[i][0] = _w;
			wv[i][1] = _v;
		}
	}

	private static void solve() {
//		dp = new long[P + 1][C + 1];
//		visited = new boolean[P + 1][C + 1];
		Arrays.sort(wv, (a, b) -> {
			long diff = (long) b[1] * a[0] - (long) a[1] * b[0];
			if (diff > 0)
				return 1;
			if (diff == 0)
				return 0;
			return -1;
		});
		max = 0;
		dfs(0, 0, C);
		ret.append(max);
	}

	private static void dfs(int i, long v, long remain) {
		if (max < v) {
			max = v;
//			System.out.println(i + " " + v + " " + remain + " " + max);
		}
		if (i == P || remain == 0)
			return;
		long p = promise(i + 1, remain);
		if (v + p <= max)
			return;
		if (remain - wv[i + 1][0] >= 0)
			dfs(i + 1, v + wv[i + 1][1], remain - wv[i + 1][0]);
		dfs(i + 1, v, remain);
	}

	private static long promise(int i, long remain) {
		long res = 0;
		while (i <= P && remain - wv[i][0] >= 0) {
			res += wv[i][1];
			remain -= wv[i][0];
			i++;
		}
		if (i <= P)
			res += remain * wv[i][1] / wv[i][0];
		return res;
	}
}
