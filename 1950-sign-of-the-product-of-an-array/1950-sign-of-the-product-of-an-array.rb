# @param {Integer[]} nums
# @return {Integer}
def array_sign(nums)

    sign = true # true for pos and false for neg
    nums.each do |num|
        return 0 if num == 0

        if num > 0
            sign = sign == false ? false : true
        else
            sign = sign == false ? true : false
        end
    end

    sign ? 1 : -1
end