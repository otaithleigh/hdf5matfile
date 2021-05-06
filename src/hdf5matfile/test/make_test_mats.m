%% Cells
clear c1 c2

c1 = {1, 2, 3};
c2 = {[1 2 3 4], [5 6 7 8]};
c3 = {[1 2 3 4], [5 6 7 8]
      [4 3 2 1], [8 7 6 5]};

save 'test_cells.mat' c1 c2 c3 -v7.3

%% Structs
clear s1 s2 s3

% Simple struct
s1 = struct('a', 3, 'b', 'foobar');

% Non-scalar struct
s2(2) = struct();
s2(1).a = 1;
s2(2).a = 2;
s2(1).b = 'foo';
s2(2).b = 'bar';

% Nested struct
s3.s1 = s1;
s3.s2 = s2;

save 'test_structs.mat' s1 s2 s3 -v7.3

%% Chars
clear ch1 ch2 ch3

ch1 = 'hello world!';
ch2 = ['hello'; 'world'];
ch3 = {'hello', 'world'};

save 'test_chars.mat' ch1 ch2 ch3 -v7.3

%% Integers
clear i8 i16 i32 i64 u8 u16 u32 u64

i8 = int8([0 -1 -2 -3 -4 -5 -6 -7]);
i16 = int16([0 -1 -2 -3 -4 -5 -6 -7]);
i32 = int32([0 -1 -2 -3 -4 -5 -6 -7]);
i64 = int64([0 -1 -2 -3 -4 -5 -6 -7]);

u8 = uint8([0 1 2 3 4 5 6 7]);
u16 = uint16([0 1 2 3 4 5 6 7]);
u32 = uint32([0 1 2 3 4 5 6 7]);
u64 = uint64([0 1 2 3 4 5 6 7]);

save 'test_integers.mat' i8 i16 i32 i64 u8 u16 u32 u64 -v7.3

%% Arrays of various sizes
clear a0 a1 a2 a3

a0 = 1;
a1 = [1 2 3];
a2 = [1 2 3 ; 4 5 6];
a3 = ones(2, 3, 4);

save 'test_arrays.mat' a0 a1 a2 a3 -v7.3

%% Empty arrays
clear e0 e1 e2

e0 = double.empty(0);
e1 = double.empty(1, 0);
e2 = double.empty(1, 1, 0);

save 'test_empty.mat' e0 e1 e2 -v7.3
