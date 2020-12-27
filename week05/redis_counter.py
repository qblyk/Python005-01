# connect Redis
import redis
import pretty_errors

client = redis.Redis(host='81.68.90.212', password='qwer!@#$1')


def counter(video_id: int):

    # set InIt Data
    client.set(str(video_id), '0', nx=True)

    # print(type(client.get(str(video_id))))

    # playCnt +1
    try:
        client.incr(str(video_id))
        count_number = client.get(str(video_id))
        print(count_number.decode())
        return count_number
    except Exception as e:
        client.delete(str(video_id))
        client.incr(str(video_id))
        print(count_number.decode())
        print(f'%d Count exception, The object has been initialized, error info：' % (
            video_id), e)
        return count_number


if __name__ == '__main__':
    counter(1003)
