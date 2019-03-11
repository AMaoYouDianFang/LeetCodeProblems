class Solution:
    def lengthLongestPath(self, input):
        lap = 0
        depth_len  = {0: 0}
        for line in  input.splitlines():  #按照行进行分割('\r', '\r\n', \n')
            name = line.lstrip('\t')        #str.lstrip([chars])截掉指定的字符串
            # 前面有几个'\t', depth就是几, 因为'\t'的长度为1
            depth = len(line) - len(name) 
            if '.' in name: #文件
                lap = max(lap, depth_len[depth] + len(name))
            else:
                # 加1是为了加上一个path分隔符'/'的长度
                depth_len[depth + 1] = depth_len[depth] + 1 + len(name)
        return lap


if __name__ == "__main__":
    s = Solution()
    res = s.lengthLongestPath("dir\n\tsubdir1000000000000\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    print(res)