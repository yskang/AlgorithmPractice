#include<bits/stdc++.h>
using namespace std;

int n;
vector<int> zip_r, zip_c;
vector<int> r_map(10001, -1), c_map(10001, -1);
vector<pair<int, int> > dots;
vector<vector<int> > land;

void draw_lines()
{
    dots.push_back(dots[0]);
    pair<int, int> prev_dot = dots[0];
    prev_dot = make_pair(r_map[prev_dot.first], c_map[prev_dot.second]);

    for (int i = 1; i < dots.size(); i++)
    {
        pair<int, int> cur_dot = dots[i];
        cur_dot = make_pair(r_map[cur_dot.first], c_map[cur_dot.second]);

        if (prev_dot.first == cur_dot.first)
        {
            for (int c = min(prev_dot.second, cur_dot.second); c < max(prev_dot.second, cur_dot.second); c++)
            {
                land[prev_dot.first][c] |= 1;
            }
        }
        else
        {
            for (int r = min(prev_dot.first, cur_dot.first); r < max(prev_dot.first, cur_dot.first); r++)
            {
                land[r][prev_dot.second] |= 8;
            }
        }
        prev_dot = cur_dot;
    }
}

int get_area(int r, int c)
{
    int area = 0;
    deque<pair<int, int> > q;
    q.push_back(make_pair(r, c));
    while (q.empty() == false)
    {
        pair<int, int> cur = q.front();
        int rr = cur.first, cc = cur.second;
        q.pop_front();
        if ((land[rr][cc] & 16) == 16)
        {
            continue;
        }
        land[rr][cc] |= 16;
        int width = zip_c[cc+1] - zip_c[cc];
        int height = zip_r[rr+1] - zip_r[rr];
        area += width * height;

        int nr = rr, nc = cc+1;
        if ( nr >= 0 && nr < land.size()-1 && nc >= 0 && nc < land[0].size()-1
            && (land[nr][nc] & 8) != 8 && (land[nr][nc] & 16) != 16)
        {
            q.push_back(make_pair(nr, nc));
        }
        nr = rr+1, nc = cc;
        if ( nr >= 0 && nr < land.size()-1 && nc >= 0 && nc < land[0].size()-1
            && (land[nr][nc] & 1) != 1 && (land[nr][nc] & 16) != 16)
        {
            q.push_back(make_pair(nr, nc));
        }
        nr = rr, nc = cc-1;
        if ( nr >= 0 && nr < land.size()-1 && nc >= 0 && nc < land[0].size()-1
            && (land[rr][cc] & 8) != 8 && (land[nr][nc] & 16) != 16)
        {
            q.push_back(make_pair(nr, nc));
        }
        nr = rr-1, nc = cc;
        if ( nr >= 0 && nr < land.size()-1 && nc >= 0 && nc < land[0].size()-1
            && (land[rr][cc] & 1) != 1 && (land[nr][nc] & 16) != 16)
        {
            q.push_back(make_pair(nr, nc));
        }
    }
    return area;
}

void solution()
{
    int max_area = 0, area = 0;
    set<int> set_r, set_c;
    for (pair<int, int> dot: dots)
    {
        set_r.insert(dot.first);
        set_c.insert(dot.second);
    }
    zip_r = vector<int>(set_r.begin(), set_r.end());
    zip_c = vector<int>(set_c.begin(), set_c.end());

    int idx = 0;
    for (int r: zip_r)
    {
        r_map[r] = idx;
        idx++;
    }
    idx = 0;
    for (int c: zip_c)
    {
        c_map[c] = idx;
        idx++;
    }

    land = vector<vector<int> >(zip_r.size()+2, vector<int>(zip_c.size()+2, 0));

    draw_lines();

    zip_r.push_back(0);
    zip_r.push_back(0);
    zip_c.push_back(0);
    zip_c.push_back(0);
    
    for (int r = zip_r.size()-2; r >= 0; r--)
    {
        for (int c = zip_c.size()-2; c >= 0; c--)
        {
            if ((land[r][c] & 16) == 16)
            {
                continue;
            }
            area = get_area(r, c);
            max_area = max(max_area, area);
        }
    }

    cout << max_area << endl;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n;
    int x, y;
    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        dots.push_back(make_pair(x, y));
    }
    solution();   
    return 0;
}
